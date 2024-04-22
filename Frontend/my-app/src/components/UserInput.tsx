import React from 'react';

interface UserInputProps {
    value: string;
    onChange: (event: React.ChangeEvent<HTMLTextAreaElement>) => void; // Adjusted to handle textarea
}

const UserInput: React.FC<UserInputProps> = ({ value, onChange }) => {
    const speak = (text: string) => {
        // Stop any current speech before starting new speech
        window.speechSynthesis.cancel();
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
        <div>
            <textarea
                className="w-full p-2 border rounded"
                value={value}
                onChange={onChange}
                rows={4}
                placeholder="Enter your text here..."
            ></textarea>
            <button onClick={() => speak(value)} className="ml-2 p-2 bg-blue-500 text-white rounded">Speak Input</button>
            <button onClick={pauseSpeak} className="ml-2 p-2 bg-gray-500 text-white rounded">Pause</button>
            <button onClick={resumeSpeak} className="ml-2 p-2 bg-green-500 text-white rounded">Resume</button>
        </div>
    );
};

export default UserInput;
