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

    # interface.interface_develop_model.run_test('/home/user/Documents/006_0.025mg_ml_001','006_0.025mg_ml_001')
    # interface.interface_develop_model.run_test('/home/user/Documents/006_0.025mg_ml_002','006_0.025mg_ml_002')
    # interface.interface_develop_model.run_test('/home/user/Documents/006_0.025mg_ml_003','006_0.025mg_ml_003')
    # interface.interface_develop_model.run_test('/home/user/Documents/007_002','007_002')
    # interface.interface_develop_model.run_test('/home/user/Documents/007_003','007_003')
    # interface.interface_develop_model.run_test('/home/user/Documents/007_004','007_004')
    # interface.interface_develop_model.run_test('/home/user/Documents/008_1mg_ml_001_1CC','008_1mg_ml_001_1CC')
    # interface.interface_develop_model.run_test('/home/user/Documents/008_1mg_ml_002_2CC','008_1mg_ml_002_2CC')
    # interface.interface_develop_model.run_test('/home/user/Documents/008_1mg_ml_003_2CC','008_1mg_ml_003_2CC')
    # interface.interface_develop_model.run_test('/home/user/Documents/009_001_a','009_001_a')
    interface.interface_develop_model.run_test('/home/user/Documents/009_001_af','009_001_af')
    # interface.interface_develop_model.run_test('/home/user/Documents/009_001_afr','009_001_afr')
    # interface.interface_develop_model.run_test('/home/user/Documents/009_002_f','009_002_f')
    # interface.interface_develop_model.run_test('/home/user/Documents/009_002_ff','009_002_ff')
    # interface.interface_develop_model.run_test('/home/user/Documents/009_002_ffr','009_002_ffr')
    # interface.interface_develop_model.run_test('/home/user/Documents/011_5mg_ml_1CC_001','011_5mg_ml_1CC_001')
    # interface.interface_develop_model.run_test('/home/user/Documents/011_5mg_ml_1CC_002','011_5mg_ml_1CC_002')
    # interface.interface_develop_model.run_test('/home/user/Documents/011_5mg_ml_1CC_004','011_5mg_ml_1CC_004')

if __name__ == '__main__':
    # main()

    debug_mode()