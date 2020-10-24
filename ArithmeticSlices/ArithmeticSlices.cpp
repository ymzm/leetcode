public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int ret = 0;
        int diff = 0;
        int diff2 = 0;
        int length = A.size();
        int alive = 0;
        if (length < 3)
        {
            return 0;
        }
        diff=A[1]-A[0];
        for (int i=2; i<length; i++)
        {
            diff2 = A[i]-A[i-1];
            if ( diff2 == diff)
            {
                ret = ret + alive +1;
                alive++;
            }
            else
            {
                alive = 0;
                diff = diff2;
            }
        }
        
        return ret;
    }
};
