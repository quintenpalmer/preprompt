from src.view.view import View
from src.model.model import Model
from src.util import make_logger

if __name__ == '__main__':
	make_logger()
	model = Model()
	view = View(model)
	view.run()
