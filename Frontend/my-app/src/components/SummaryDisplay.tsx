import React from 'react';

const SummaryDisplay: React.FC<{ summary: string }> = ({ summary }) => {
    const speak = (text: string) => {
        window.speechSynthesis.cancel(); // Stop any current speech
        const speech = new SpeechSynthesisUtterance(text);
        window.speechSynthesis.speak(speech);
    };

    const pauseSpeak = () => {
        window.speechSynthesis.pause(); // Pauses speaking
    };

    const resumeSpeak = () => {
        window.speechSynthesis.resume(); // Resumes speaking
    };

    return (
        <div className="p-2 border rounded bg-gray-100">
            <div>{summary || "The summary will appear here..."}</div>
            <button onClick={() => speak(summary)} className="mt-2 ml-2 p-2 bg-blue-500 text-white rounded">Speak Summary</button>
            <button onClick={pauseSpeak} className="mt-2 ml-2 p-2 bg-gray-500 text-white rounded">Pause</button>
            <button onClick={resumeSpeak} className="mt-2 ml-2 p-2 bg-green-500 text-white rounded">Resume</button>
        </div>
    );
};

export default SummaryDisplay;
