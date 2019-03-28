from Base import Base
from main.model.Deploy import deploys

class DeployService(Base):
    __model__ = deploys
deployService = DeployService()