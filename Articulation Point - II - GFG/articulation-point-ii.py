class Solution:
	def articulationPoints(self, V, adj):
		#Code here
		global timer
        timer=0
        dis=[0]*V
        low=[0]*V
        visited=[False]*V
        ap=[False]*V
        parent=[None]*V
        res=[]
        
        for i in range(V):
            if visited[i]==False:
                self.fun(i,dis,low,ap,V,adj,visited,parent)
        
        res=[]
        flag=0
        for i in range(V):
            if ap[i]==True:
                res.append(i)
                flag=1
        if flag==0:
            return [-1]
        return res
        
    def fun(self, u, dis, low, ap, V, adj, visited, parent):
        global timer
        visited[u]=True
        timer=timer+1
        dis[u]=timer
        low[u]=timer
        children=0
        for v in adj[u]:
            if visited[v]==False:
                children+=1
                parent[v]=u
                self.fun(v, dis, low, ap, V, adj, visited, parent)
                low[u]=min(low[u],low[v])
                
                if parent[u]==None and children>1:
                    ap[u]=True
            
                if parent[u]!=None and low[v]>=dis[u]:
                    ap[u]=True
            elif v!=parent[u]:
                low[u]=min(low[u],dis[v])

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.articulationPoints(V, adj)
		for i in ans:
			print(i, end = " ")
		print()
# } Driver Code Ends