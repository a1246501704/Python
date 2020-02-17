
# 绝对导入
# from glance_v1.api.policy import get
# from glance_v1.api.versions import create_resource
# from glance_v1.cmd.manage import main
# from glance_v1.db.models import register_models


#相对导入
from .api.policy import get
from .api.versions import create_resource
from .cmd.manage import main
from .db.models import register_models




