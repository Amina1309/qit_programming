export type Matrix = number[][];

export interface DecompositionResult {
  L?: Matrix;
  U?: Matrix;
  Q?: Matrix;
  R?: Matrix;
  error?: string;
}

export interface MatrixState {
  inputMatrix: Matrix;
  decompositionType: 'LU' | 'QR';
  result: DecompositionResult | null;
  loading: boolean;
  error: string | null;
}