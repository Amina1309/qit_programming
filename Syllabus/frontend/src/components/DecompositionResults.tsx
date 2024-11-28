import React from 'react';
import { 
  Paper, 
  Typography, 
  Table, 
  TableBody, 
  TableCell, 
  TableContainer, 
  TableHead, 
  TableRow, 
  CircularProgress, 
  Alert 
} from '@mui/material';
import { useAppSelector } from '../store/hooks';

const DecompositionResults: React.FC = () => {
  const { result, loading, error, decompositionType } = useAppSelector(state => state.matrix);

  const renderMatrix = (matrix?: number[][]) => {
    if (!matrix) return <Typography>No matrix to display</Typography>;

    return (
      <TableContainer component={Paper}>
        <Table size="small">
          <TableBody>
            {matrix.map((row, rowIndex) => (
              <TableRow key={rowIndex}>
                {row.map((cell, colIndex) => (
                  <TableCell key={colIndex} align="right">
                    {cell.toFixed(4)}
                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    );
  };

  if (loading) return <CircularProgress />;
  if (error) return <Alert severity="error">{error}</Alert>;

  return (
    <Paper elevation={3} sx={{ p: 3, mt: 2 }}>
      <Typography variant="h6">
        {decompositionType} Decomposition Results
      </Typography>
      {decompositionType === 'LU' && result && (
        <>
          <Typography variant="subtitle1">L Matrix:</Typography>
          {renderMatrix(result.L)}
          <Typography variant="subtitle1" sx={{ mt: 2 }}>U Matrix:</Typography>
          {renderMatrix(result.U)}
        </>
      )}
      {decompositionType === 'QR' && result && (
        <>
          <Typography variant="subtitle1">Q Matrix:</Typography>
          {renderMatrix(result.Q)}
          <Typography variant="subtitle1" sx={{ mt: 2 }}>R Matrix:</Typography>
          {renderMatrix(result.R)}
        </>
      )}
    </Paper>
  );
};

export default DecompositionResults;