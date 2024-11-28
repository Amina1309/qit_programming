from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from .matrix_operations import MatrixDecomposition

@csrf_exempt
@require_http_methods(["POST"])
def lu_decompose(request):
    """
    Endpoint for LU Decomposition
    Expects JSON with 'matrix' key containing 2D matrix
    """
    try:
        data = json.loads(request.body)
        matrix = data.get('matrix', [])
        
        if not matrix or not isinstance(matrix, list):
            return JsonResponse({
                'error': 'Invalid matrix input'
            }, status=400)
        
        L, U = MatrixDecomposition.lu_decomposition(matrix)
        
        return JsonResponse({
            'L': L,
            'U': U
        })
    
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def qr_decompose(request):
    """
    Endpoint for QR Decomposition
    Expects JSON with 'matrix' key containing 2D matrix
    """
    try:
        data = json.loads(request.body)
        matrix = data.get('matrix', [])
        
        if not matrix or not isinstance(matrix, list):
            return JsonResponse({
                'error': 'Invalid matrix input'
            }, status=400)
        
        Q, R = MatrixDecomposition.qr_decomposition(matrix)
        
        return JsonResponse({
            'Q': Q,
            'R': R
        })
    
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)