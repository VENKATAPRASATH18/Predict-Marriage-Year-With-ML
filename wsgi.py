from Flask_App import F_app
import os 

port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
        F_app.run(host='0.0.0.0', port=port, debug=True)
