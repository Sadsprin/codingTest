#include <iostream>
#include <vector>

#define INF 1e9

using namespace std;

int n, m, start;

vector<pair<int, int>> graph[100001];

bool visited[100001];

int d[100001];

int get_shortest_node(){
    int min_value = INF;
    int index = 0;
    for(int i = 1; i <= n; i++){
        if (d[i] < min_value & !visited[i]){
            min_value = d[i];
            index = i;
        }
    }
    return index;
}

void dijkstra(int start){
    d[start] = 0;
    visited[start] = true;
    for(int i = 0; i < graph[start].size(); i++){
        d[graph[start][i].first] = graph[start][i].second;
    }
    for(int j = 0; j < n - 1; j++){
        int now;
        now = get_shortest_node();
        visited[now] = true;
        for(int k = 0; k < graph[now].size(); k++){
            if(d[now] + graph[now][k].second < d[graph[now][k].first]){
                d[graph[now][k].first] = d[now] + graph[now][k].second;
            }
        }
    }
}




int main(void){
    cin >> n >> m >> start;

    for(int i = 0; i < m; i++){
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
    }
    fill_n(d, 100001, INF);
    fill_n(visited, 100001, false);
    dijkstra(start);
    
    for (int i = 1; i <= n; i++){
        if(d[i] == INF){
            cout << "INFINITY" << endl;
        }
        else{
            cout << d[i] << endl;
        }
    }


    return 0;

}