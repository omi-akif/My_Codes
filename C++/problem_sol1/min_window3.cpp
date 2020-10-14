#include <iostream>
#include <string>
#include <unordered_map>
#include <climits>
#include <algorithm>

using namespace std;


int main(){

    string s = "this is geek";
    string t = "sek";

    s.erase(remove_if(s.begin(), s.end(), ::isspace), s.end());

    unordered_map<char, int> s_ta_map;

    int len = INT_MAX;
    int start_p = 0, end_p = 0;

    char end_char;
    int start_char;
    

    for(char c : t){
        s_ta_map[c]++;
    }

    int count_m = s_ta_map.size();
    string result = "";

    while(end_p < s.length()){
        end_char = s[end_p];

        if(s_ta_map.find(end_char) != s_ta_map.end()){
            s_ta_map[end_char]--;

            if(s_ta_map[end_char] == 0){
                count_m--;
            }
        }

        end_p ++;

        while(count_m == 0){
            if ((end_p-start_p) < len){
                len = end_p - start_p;
                result = s.substr(start_p, end_p-start_p);
            }


            start_char = s[start_p];

            if(s_ta_map.count(start_char) == 1){
                s_ta_map[start_char]++;
                if(s_ta_map[start_char] > 0){
                    count_m++;
                }
            }
            
            start_p++;
        }
    }

    cout << result << endl;

}
