import pytest

from leapp.libraries.common.config import version
from leapp.models import CryptoPolicyInfo


@pytest.mark.parametrize(('target_version', 'should_run'), [
    ('8', False),
    ('9', True),
    ('10', True),
])
def test_actor_execution(monkeypatch, current_actor_context, target_version, should_run):
    monkeypatch.setattr(version, 'get_target_major_version', lambda: target_version)
    current_actor_context.run()
    if should_run:
        assert current_actor_context.consume(CryptoPolicyInfo)
