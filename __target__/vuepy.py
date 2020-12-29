Vue=require("vue")["default"]
class VuePy:
	"""docstring for VuePy"""
	methods=[]
	computed=[]
	watch=[]
	delimiters=['[[', ']]']
	__deployed__=False
	def __init__(self,*args,**kwargs):
		data={"methods":{},
			  "watch":{},
			  "compute":{}}

		for elem in dir(self):
			if elem not in ['__bases__', '__class__', '__init__', 
							'__metaclass__', '__module__', '__name__', 
							'__new__',"methods","computed",
							"watch","mount","deploy","__deployed__"]:
			
				if typeof(getattr(self,elem))=="function":
					getattr(self,elem).__name__=elem

				if elem in self.methods:
					data["methods"][elem]=getattr(self,elem)
				elif elem in self.compute:
					data["computed"][elem]=getattr(self,elem)
				elif elem in self.watch:
					data["watch"][elem]=getattr(self,elem)
				else:
					data[elem]=getattr(self,elem)
		self.__component__=data
	
	def deploy(self):
		self.vue=__new__(Vue(self.__component__))
		self.__deployed__=True
		return self

	def mount(self,el):
		if not self.__deployed__:
			self.deploy()
		self.vue["$mount"](el)