import sys

class node:
	def __init__(self,id,outgoing_edges):
		self.id=id
		self.outgoing_edges=outgoing_edges

class edge:
	def __init__(self,id,start_node,end_node,global_var,type_of_edge,trans_func):
		self.id=id
		self.start_node=start_node
		self.end_node=end_node
		self.global_var=global_var
		self.type_of_edge=type_of_edge
		self.trans_func=trans_func


class graph:
	def __init__(self,nodes,edges,local_var):
		self.local_var=local_var
		self.nodes=nodes
		self.edges=edges

class process:
    def _init_(self,graph_id,curr_state):
    	self.graph_id=graph_id
    	self.curr_state=curr_state
    	self.local_var=cfd_list[graph_id].local_var




def read_cfd(s):
	cfd = open(s, "r")
	line_no=1
	temp_graph=graph([],[],{})

	for rows in open(s):
		if line_no==1:
			i=0
			while i<int(rows):
				temp_node=node(i,[])
				temp_graph.nodes.append(temp_node)
				i=i+1
			continue	

		if line_no==2:
			loc_var_size=int(rows)
			continue
		if	line_no<=loc_var_size+2:
			lstrip_rows=rows.lstrip()
			if lstrip_rows[0]=='[':
				split_rows=lstrip_rows.split()
				i=0
				while i< int(split_rows[3]):
					var_name=split_rows[4]+str(i)
					temp_graph.local_var[var_name]=int(split_rows[5])
					i=i+1
			else:
				exec("temp_graph."+rows.strip())
			continue
		rows=rows.strip().split()
		if rows[0]!='t':
			temp_edge=edge(int(rows[0]),int(rows[1]),int(rows[2]),rows[3],rows[4],[])
			temp_graph.nodes[int(rows[1])].outgoing_edges=len(temp_graph.edges)
			if rows[4]!='w':
				temp_edge.trans_func.append(rows[5])
			else:
				i=5
				while i < len(rows):
					temp_edge.trans_func.append(rows[i])
					i=i+1
			temp_graph.edges.append(temp_edge)
		line_no=line_no+1	
	cfd_list.append(temp_graph)				

def process_read(s):
	for rows in open(s):
		if


cfd_list=[];
process_list=[];

i=1
while i<len(sys.argv)-1:
	read_cfd(sys.argv[i])
	i=i+1

read_process(sys.argv[i])
