<<<<<<< HEAD
from app import create_app
from app.services.facade import HBnBFacade

app = create_app()
facade = HBnBFacade

if __name__ == '__main__':
    app.run(debug=True, port=5011)
=======
from app import create_app
from app.services.facade import HBnBFacade

app = create_app()
facade = HBnBFacade()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
>>>>>>> d7f9101b3ca1e9889fd68e24f20781558c2d7b40
