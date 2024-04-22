import React, { useState } from 'react';
import NeuroTypeDropdown from './components/NeuroTypeDropdown';
import UserInput from './components/UserInput';

interface InputFormProps {
  neuroType: string;
  setUserInput: React.Dispatch<React.SetStateAction<string>>;
  setNeuroType: React.Dispatch<React.SetStateAction<string>>;
  fetchSummary: () => Promise<void>;
}

const InputForm: React.FC<InputFormProps> = ({ neuroType, setUserInput, setNeuroType, fetchSummary }) => {
  // This assumes that UserInput is for entering text that will be summarized.
  // If so, you should have a state here for handling this user input.
  const [inputText, setInputText] = useState(''); // Added state for user input text.

  return (
    <div>
      <NeuroTypeDropdown onChange={e => setNeuroType(e.target.value)} />
      <UserInput value={inputText} onChange={e => setInputText(e.target.value)} /> {/* Adjusted to use the new state */}
      <button onClick={fetchSummary}>Fetch General Summary</button>
    </div>
  );
};

export default InputForm;
