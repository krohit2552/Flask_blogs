from app import app
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Starting Waitress server...")
    
    from waitress import serve
    serve(app, host="localhost", port=5000)
