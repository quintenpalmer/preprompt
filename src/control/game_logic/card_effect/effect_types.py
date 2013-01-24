import abc

class Abstract_Instant_Effect:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def apply_to(self,action):
		pass

class Abstract_Instant_Cond:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def is_valid(self,action):
		pass

class Abstract_Persist_Cond:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def tick(self,action,game,uid):
		pass

	@abc.abstractmethod
	def persists(self,action,game,uid):
		pass

	@abc.abstractmethod
	def reset(self,action,game,uid):
		pass
