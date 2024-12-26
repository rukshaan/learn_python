
from Weather import create_app

# Create the app instance using create_app()
app = create_app()

if __name__ == '__main__':
    # Only call app.run() once, no need to call create_app() here again
    app.run(debug=True)
