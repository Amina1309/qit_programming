import axios from 'axios';
import { Matrix } from '../types/matrix';

const API_BASE_URL = 'http://localhost:8000/api';

export const matrixService = {
  async luDecompose(matrix: Matrix) {
    try {
      const response = await axios.post(`${API_BASE_URL}/lu-decompose/`, { matrix });
      return response.data;
    } catch (error) {
      console.error('LU Decomposition Error:', error);
      throw error;
    }
  },

  async qrDecompose(matrix: Matrix) {
    try {
      const response = await axios.post(`${API_BASE_URL}/qr-decompose/`, { matrix });
      return response.data;
    } catch (error) {
      console.error('QR Decomposition Error:', error);
      throw error;
    }
  }
};