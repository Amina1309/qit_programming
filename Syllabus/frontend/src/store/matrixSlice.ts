import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';
import { MatrixState, Matrix, DecompositionResult } from '../types/matrix';
import { matrixService } from '../services/apiService';

const initialState: MatrixState = {
  inputMatrix: [
    [0, 0],
    [0, 0]
  ],
  decompositionType: 'LU',
  result: null,
  loading: false,
  error: null
};

export const performDecomposition = createAsyncThunk(
  'matrix/decompose',
  async ({ matrix, type }: { matrix: Matrix; type: 'LU' | 'QR' }, { rejectWithValue }) => {
    try {
      if (type === 'LU') {
        return await matrixService.luDecompose(matrix);
      } else {
        return await matrixService.qrDecompose(matrix);
      }
    } catch (error: any) {
      return rejectWithValue(error.response?.data || 'Decomposition failed');
    }
  }
);

const matrixSlice = createSlice({
  name: 'matrix',
  initialState,
  reducers: {
    setInputMatrix: (state, action: PayloadAction<Matrix>) => {
      // Create a new array to avoid mutating the original state
      state.inputMatrix = action.payload.map(row => [...row]);
    },
    updateMatrixCell: (state, action: PayloadAction<{
      rowIndex: number;
      colIndex: number;
      value: number;
    }>) => {
      // Create a new matrix to avoid direct mutation
      const newMatrix = state.inputMatrix.map(row => [...row]);
      newMatrix[action.payload.rowIndex][action.payload.colIndex] = action.payload.value;
      state.inputMatrix = newMatrix;
    },
    setDecompositionType: (state, action: PayloadAction<'LU' | 'QR'>) => {
      state.decompositionType = action.payload;
    },
    resetResult: (state) => {
      state.result = null;
      state.error = null;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(performDecomposition.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(performDecomposition.fulfilled, (state, action) => {
        state.loading = false;
        state.result = action.payload;
      })
      .addCase(performDecomposition.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      });
  }
});

export const { 
  setInputMatrix, 
  updateMatrixCell, 
  setDecompositionType, 
  resetResult 
} = matrixSlice.actions;
export default matrixSlice.reducer;