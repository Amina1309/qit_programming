import React from 'react';
import { Provider } from 'react-redux';
import { CssBaseline, Container } from '@mui/material';
import { store } from './store';
import MatrixInput from './components/MatrixInput';
import DecompositionResults from './components/DecompositionResults';

const App: React.FC = () => {
  return (
    <Provider store={store}>
      <CssBaseline />
      <Container maxWidth="md">
        <MatrixInput />
        <DecompositionResults />
      </Container>
    </Provider>
  );
};

export default App;