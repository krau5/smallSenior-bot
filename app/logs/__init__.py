# from config import dp
import logging

logging.basicConfig(
    handlers=[logging.FileHandler('logs/app.log', 'a', 'utf-8')],
    format='%(asctime)% - %(levelname)% - %(message)%',
    datefmt="%d-%m-%y %H:%M",
    level=logging.INFO
)
logger = logging.getLogger('app')
