from src.view.view import View
from src.model.model import Model

if __name__ == '__main__':
	model = Model()
	view = View(model)
	view.run()
