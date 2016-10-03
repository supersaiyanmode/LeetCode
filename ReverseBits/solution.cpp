class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        for (int i=0; i<32; i++) {
            uint32_t bit = (1 <<i) & n;
            if (bit)
                res |= 1 << (32 - i - 1);
        }
        return res;
    }
};