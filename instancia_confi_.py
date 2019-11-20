
from alembic import op
from flaskps.configurations.models import Configurations
from flaskps import db

revision = 'crea_config'
down_revision = '5d1ba61d2b9d'
branch_labels = None
depends_on = None


def upgrade():
    conf = Configurations(
        active=True,
        description="escuela orquesta",
        title="escuela orquesta",
        email="eber@mail.com",
        paginator_offset=20,
    )
    db.session.add(conf)
    db.session.commit()


def downgrade():
    pass
