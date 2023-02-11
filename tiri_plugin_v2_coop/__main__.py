import logging
import datetime

def main():
    print('main is running')
    try:
        # logging.debug('debug')
        # logging.info('info')
        # logging.warning('warning')
        # logging.error('error')
        # logging.critical('critical')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
            datefmt='%Y%m%d %H:%M:%S')

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)

        log_filename = './log/'+datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")
        fh = logging.FileHandler(log_filename)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)

        # Generating UI
        import ui.home

        # #================================
        # import interface.interface
        # interface.interface.interfaceDBScan().doDBScan(709,709)
    except Exception as e :
        print('ERROR exited')
        print(e)



def develop_model():
    print('develop model')
    try:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
            datefmt='%Y%m%d %H:%M:%S')

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)

        log_filename = './log/'+datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")
        fh = logging.FileHandler(log_filename)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)

        import interface.interface_develop_model

        interface.interface_develop_model.run_test()

    except Exception as e:
        print('ERROR exited')
        print(e)


def debug_mode():

    print('develop model')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
        datefmt='%Y%m%d %H:%M:%S')

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    log_filename = './log/'+datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")
    fh = logging.FileHandler(log_filename)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    import interface.interface_develop_model

    # input : (path_raw_data,path_packing_dst_folder)
    interface.interface_develop_model.run_test('/Users/user/Documents/DATA/RAW/005_0025mg_ml_001','/Users/user/Documents/GitHub/tiri_pulgin_v2/005_0025_001')

if __name__ == '__main__':
    # main()

    debug_mode()