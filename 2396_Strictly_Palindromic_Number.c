class Solution {
public:
    bool isStrictlyPalindromic(int n) {
        /* int based[n-3];
        for (int i=0; i<(n-3); i++)
        {
            //cout << i;
            based[i]=0;
        }
        */
        for (int i=0; i<(n-2); i++)
        {
            int ii=i+2;
            int j=0;
            while (pow(ii,j)<=n)
            {
                j++;
            }
            j=j-1;
            //cout << j << " ";
            int k=n;
            int based[j+1];
            for (int u=0; u<j+1; u++)
            {
                //cout << i;
                based[u]=0;
                //cout << based[u];
            }
            //cout << " ";
            for (int l=0; l<j+1; l++)
            {
                //cout << l <<" ";
                //cout << k <<" ";
                for (int m=1; m<ii+1; m++)
                {
                    //cout << "m="<< ii-m;
                    if (k>=pow(ii,j-l)*(ii-m))
                    {
                        based[l]=ii-m;
                        break;
                    }
                }
                //cout << " ";
                /*if (k>=pow(ii,j-l))
                    based[l]=1;
                    else based[l]=0;
                */
                k=k-pow(ii,j-l)*based[l];
            }
            for (int l=0; l<j+1; l++)
                //cout << based[l];
            cout << endl;
            for (int l=0; l<(j/2+1);l++)
            {
                //cout << based[l]<<"="<<based[j-l]<<" ";
                if (based[l]!=based[j-l])
                return (0);
            }
            //cout << endl;
        }
        return (1);
    }
};
