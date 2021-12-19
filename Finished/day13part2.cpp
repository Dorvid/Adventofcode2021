#include <iostream>
#include <fstream>
#include <string>
#include <vector>

void print_arr(std::vector<std::vector<char>> a){
    for(unsigned i = 0; i < a.size();i++){
        for(unsigned j = 0; j < a[0].size();j++){  
            std::cout << a[i][j];
        }
        std::cout << std::endl;
    }
}



void fold(std::vector<std::vector<char>> &a,char c,unsigned middle,unsigned max_x,unsigned max_y){
    std::cout << "Doing fold " << c << " " << middle << std::endl;
    // unsigned width = array[0].size();
    // unsigned height = array.size();
    // std::cout << "Width: " << width << " Height: " << height << std::endl;
    std::vector<std::vector<char>> new_paper_arr;
    if(c == 'x'){
        // for(unsigned i = 0; i < max_y;i++){
        //     a[i][middle] = '|';
        // }
        for(unsigned i = 0; i < a.size();i++){
            std::vector<char> v;
            for(unsigned j = 0; j < middle;j++){  
                if(a[i][j] == '#' || a[i][max_x -1-j] == '#'){
                    v.push_back('#');
                }
                else{
                    v.push_back('.');
                }
            }
            new_paper_arr.push_back(v);
        }

    }
    else{
        // for(unsigned i = 0; i < max_y;i++){
        //     a[middle][i] = '-';
        // }
        for(unsigned i = 0; i < middle;i++){
            std::vector<char> v;
            for(unsigned j = 0; j < a[0].size();j++){  
                if(a[i][j] == '#' || a[max_y-1 - i][j] == '#'){
                    v.push_back('#');
                }
                else{
                    v.push_back('.');
                }
            }
            new_paper_arr.push_back(v);
        }
    }
    std::cout << "Done with fold.\n";
    a.clear();
    a = new_paper_arr;
}




int main(){
    std::vector<std::pair<char,unsigned>> f_i{};
    std::ifstream fold_file;
    fold_file.open("inputDay13fold.txt");
    unsigned max_x = 0;
    unsigned max_y = 0;
    while(true)
    {
        char c;
        unsigned d;
        fold_file >> c >> d;
        f_i.push_back(std::make_pair(c,d));
        if(c == 'x' && d*2+1 > max_x){
            max_x = d*2+1;
        }
        else if(d*2+1 > max_y){
            max_y = d*2+1;
        }
        if(fold_file.eof()) break;
        std::cout << "Inputed: " << c << " and: "<<d << std::endl;
    }
    
    std::vector<std::vector<char>> paper_array;
    //paper_array[y][x]
    for(unsigned y = 0; y < max_y; y++){
        std::vector <char> v;
        for(unsigned x = 0; x < max_x; x++){
            v.push_back('.');
        }
        paper_array.push_back(v);
    }
    std::ifstream dot_file;
    dot_file.open("inputDay13.txt");
    while(true){
        int a;
        int b;
        dot_file >> a >> b;
        paper_array[b][a] = '#';
        if(dot_file.eof()) break;
    }
    std::cout << "Folding\n";
    for(auto i: f_i){
        std::cout << i.first << i.second <<std::endl;
    }
    for(unsigned i = 0;i < f_i.size();i++){
        fold(paper_array,f_i[i].first,f_i[i].second,max_x,max_y);
        if(f_i[i].first == 'x'){
            max_x = f_i[i].second;
        }
        else{
            max_y = f_i[i].second;
        }
    }
    print_arr(paper_array);
    return 0;
}