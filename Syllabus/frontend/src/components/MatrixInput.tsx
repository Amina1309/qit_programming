import React, { useState } from 'react';
import { 
  TextField, 
  Button, 
  Select, 
  MenuItem, 
  FormControl, 
  InputLabel, 
  Grid, 
  Paper, 
  Typography 
} from '@mui/material';

import { useAppDispatch, useAppSelector } from '../store/hooks';
import { 
  setInputMatrix, 
  updateMatrixCell,
  setDecompositionType, 
  performDecomposition 
} from '../store/matrixSlice';

const MatrixInput: React.FC = () => {
  const dispatch = useAppDispatch();
  const { inputMatrix, decompositionType } = useAppSelector(state => state.matrix);
  const [rows, setRows] = useState(2);
  const [cols, setCols] = useState(2);

  const handleMatrixChange = (rowIndex: number, colIndex: number, value: string) => {
    const numValue = parseFloat(value) || 0;
    dispatch(updateMatrixCell({ rowIndex, colIndex, value: numValue }));
  };

  const handleResize = () => {
    const newMatrix = Array.from({ length: rows }, () => 
      Array.from({ length: cols }, () => 0)
    );
    dispatch(setInputMatrix(newMatrix));
  };

  const handleDecompose = () => {
    dispatch(performDecomposition({ 
      matrix: inputMatrix, 
      type: decompositionType 
    }));
  };

  return (
    <Paper elevation={3} sx={{ p: 3, mt: 2 }}>
      <Typography variant="h5" gutterBottom>
        Matrix Decomposition
      </Typography>
      
      <Grid container spacing={2} alignItems="center">
        <Grid item xs={6}>
          <TextField
            label="Rows"
            type="number"
            value={rows}
            onChange={(e) => setRows(parseInt(e.target.value))}
            inputProps={{ min: 1, max: 10 }}
          />
        </Grid>
        <Grid item xs={6}>
          <TextField
            label="Columns"
            type="number"
            value={cols}
            onChange={(e) => setCols(parseInt(e.target.value))}
            inputProps={{ min: 1, max: 10 }}
          />
        </Grid>
        <Grid item xs={12}>
          <Button variant="outlined" onClick={handleResize}>
            Resize Matrix
          </Button>
        </Grid>
      </Grid>

      <Grid container spacing={2} sx={{ mt: 2 }}>
        {inputMatrix.map((row, rowIndex) => (
          <Grid item container spacing={1} key={rowIndex}>
            {row.map((cell, colIndex) => (
              <Grid item key={colIndex}>
                <TextField
                  type="number"
                  value={cell}
                  onChange={(e) => handleMatrixChange(rowIndex, colIndex, e.target.value)}
                  variant="outlined"
                  size="small"
                  sx={{ width: 70 }}
                />
              </Grid>
            ))}
          </Grid>
        ))}
      </Grid>

      <Grid container spacing={2} sx={{ mt: 2 }}>
        <Grid item xs={6}>
          <FormControl fullWidth>
            <InputLabel>Decomposition Type</InputLabel>
            <Select
              value={decompositionType}
              label="Decomposition Type"
              onChange={(e) => dispatch(setDecompositionType(e.target.value as 'LU' | 'QR'))}
            >
              <MenuItem value="LU">LU Decomposition</MenuItem>
              <MenuItem value="QR">QR Decomposition</MenuItem>
            </Select>
          </FormControl>
        </Grid>
        <Grid item xs={6}>
          <Button 
            variant="contained" 
            color="primary" 
            onClick={handleDecompose}
            fullWidth
          >
            Decompose
          </Button>
        </Grid>
      </Grid>
    </Paper>
  );
};

export default MatrixInput;