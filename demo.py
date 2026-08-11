# from us_visa.logger import logging

# # logging.info("Welcome to custom log")

# import sys
# from us_visa.logger import logging
# from us_visa.exception import USvisaException

# try:
    
#     a = 1 / 0
# except Exception as e:
    
#     logging.error("Error occurred during computation")
#     raise USvisaException(e, sys)


from us_visa.pipline.training_pipeline import TrainPipeline

obj=TrainPipeline()
obj.run_pipeline()