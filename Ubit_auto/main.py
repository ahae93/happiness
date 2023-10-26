import sys
import logging
import traceback
import basic_module
 
 
# -----------------------------------------------------------------------------
# - Name : main
# - Desc : 메인
# -----------------------------------------------------------------------------
if __name__ == '__main__':
 
    # noinspection PyBroadException
    try:
        # 로그레벨 설정(DEBUG)
        basic_module.set_loglevel('D')
 
        # 종목 조회
        item_list = basic_module.get_it9ems("KRW", "BTC")
 
        # 결과 출력
        logging.info(item_list)
 
    except KeyboardInterrupt:
        logging.error("KeyboardInterrupt Exception 발생!")
        logging.error(traceback.format_exc())
        sys.exit(1)
 
    except Exception:
        logging.error("Exception 발생!")
        logging.error(traceback.format_exc())
        sys.exit(1)