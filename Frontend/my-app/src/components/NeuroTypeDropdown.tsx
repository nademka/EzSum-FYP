import React from 'react';

// Define the props expected by NeuroTypeDropdown
interface NeuroTypeDropdownProps {
    onChange: (event: React.ChangeEvent<HTMLSelectElement>) => void;
}

// Update the NeuroTypeDropdown component to accept and use the onChange prop
const NeuroTypeDropdown: React.FC<NeuroTypeDropdownProps> = ({ onChange }) => {
    return (
        <select className="p-2 border rounded" onChange={onChange}>
            <option value="ADHD">ADHD</option>
            <option value="Autism">Autism</option>
            <option value="Dyslexia">Dyslexia</option>
            {/* Additional options can be added here */}
        </select>
    );
};

export default NeuroTypeDropdown;
