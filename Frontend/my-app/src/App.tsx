import React, { useState, useEffect } from 'react';
import './App.css';
import EzSumLogo from './Ez_Sum.svg';   
import NeuroTypeDropdown from './components/NeuroTypeDropdown';
import UserInput from './components/UserInput';
import SummaryDisplay from './components/SummaryDisplay';

const App: React.FC = () => {
    const [neuroType, setNeuroType] = useState('');
    const [userInput, setUserInput] = useState('');
    const [summary, setSummary] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        if (!userInput || !neuroType) {
            setSummary('');
            return;
        }
        fetchSummaryBasedOnType();
    }, [userInput, neuroType]);

    const fetchSummaryBasedOnType = async () => {
        setIsLoading(true);
        try {
            const response = await fetch(`http://localhost:8000/summarize/${neuroType.toLowerCase()}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: userInput })
            });
            if (!response.ok) throw new Error('Failed to fetch');
            const data = await response.json();
            setSummary(data.summary);
        } catch (error) {
            console.error('Error fetching summary based on type:', error);
        } finally {
            setIsLoading(false);
        }
    };

    const fetchGeneralSummary = async () => {
        setIsLoading(true);
        try {
            const response = await fetch('http://localhost:8000/summarize/general', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: userInput })
            });
            if (!response.ok) throw new Error('Failed to fetch');
            const data = await response.json();
            setSummary(data.summary);
        } catch (error) {
            console.error('Error fetching general summary:', error);
        } finally {
            setIsLoading(false);
        }
    };


    return (
        <div className="App">
            <header className="App-header">
                <img src={EzSumLogo} alt="EZ Sum Logo" className="App-logo" />
                <h1>EZ Sum</h1>
            </header>
            <div className="p-4">
                <h2 className="text-lg font-bold">Neurodivergence Input Form</h2>
                <NeuroTypeDropdown onChange={e => setNeuroType(e.target.value)} />
                <UserInput value={userInput} onChange={e => setUserInput(e.target.value)} />
                {isLoading ? <p>Loading summary...</p> : <SummaryDisplay summary={summary} />}
                {!userInput || !neuroType ? <p>Please select a type and enter some text to see the summary.</p> : null}
                <button onClick={fetchGeneralSummary}>Fetch General Summary</button>
            </div>
        </div>
    );
};

export default App;
