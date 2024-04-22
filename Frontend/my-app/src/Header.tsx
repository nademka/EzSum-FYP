import React from 'react';
import EzSumLogo from './Ez_Sum.svg'; // Ensure the path is correct

const Header: React.FC = () => {
  return (
    <header className="App-header">
      <img src={EzSumLogo} alt="EZ Sum Logo" className="App-logo" />
      <h1>EZ Sum</h1>
    </header>
  );
};

export default Header;
