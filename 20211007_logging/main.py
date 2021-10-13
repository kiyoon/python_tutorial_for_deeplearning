import logging

logger = logging.getLogger(__name__)

def main():
    logger.info('aa')
    logger.debug('aa')
    a = 1 / 0
    logger.warning('aa')
    pass


if __name__ == '__main__':
    logging.basicConfig(format='%(name)s: %(lineno)4d - %(levelname)s - %(message)s', level='INFO')
    try:
        main()
    except Exception:
        logger.exception('Exception occurred!')
