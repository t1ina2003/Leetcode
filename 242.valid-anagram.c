/*
 * @lc app=leetcode id=242 lang=c
 *
 * [242] Valid Anagram
 */

// @lc code=start


bool isAnagram(char * s, char * t){
    int a[26] = {0}, b[26] = {0};
    countChar(s, &a);
    countChar(t, &b);
    return compareArrays(a,b,26);
}

void countChar(char *source, int target[]){
    int index;
    for(int i=0; i<strlen(source); i++){
        index = source[i] - 97;
        target[index]++;
    }
}

int compareArrays(int a[], int b[], int n) {
  int index;
  for(index = 1; index < n; index++) {
    if (a[index] != b[index]) return 0;
  }
  return 1;
}
// @lc code=end

