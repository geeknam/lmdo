import logging
import importlib

# Set up logging
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    if event['source'] == 'aws.events':
        arn_prefix, rule_name = event['resources'][0].split('/')
        prefix, module = rule_name.split('--')
        func = module.split('.')[-1]
        module = '.'.join(module.split('.')[0:-1])
        obj = importlib.import_module(module)
        return getattr(obj, func)(event, context)

    return False
