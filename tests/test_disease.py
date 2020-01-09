import pytest

from openomics.database import DisGeNet, HMDD, LncRNADisease
import pytest

from openomics.database import DisGeNet, HMDD, LncRNADisease


@pytest.fixture
def generate_DisGeNet_ftp():
    return DisGeNet(path="https://www.disgenet.org/static/disgenet_ap1/files/downloads/", curated=True)


def test_DisGeNet(generate_DisGeNet_ftp):
    assert generate_DisGeNet_ftp.data_path == "https://www.disgenet.org/static/disgenet_ap1/files/downloads/"
    assert not generate_DisGeNet_ftp.get_disease_assocs(index="gene_name").empty


@pytest.fixture
def generate_HMDD_ftp():
    return HMDD(path="http://www.cuilab.cn/static/hmdd3/data/")


def test_HMDD(generate_HMDD_ftp):
    assert generate_HMDD_ftp.data_path == "http://www.cuilab.cn/static/hmdd3/data/"
    assert not generate_HMDD_ftp.get_disease_assocs(index="gene_name").empty


@pytest.fixture
def generate_LncRNADisease_ftp():
    return LncRNADisease(path="http://www.cuilab.cn/files/images/ldd/", species="Human")


def test_LncRNADisease(generate_LncRNADisease_ftp):
    assert generate_LncRNADisease_ftp.data_path == "http://www.cuilab.cn/files/images/ldd/"
    assert not generate_LncRNADisease_ftp.get_disease_assocs(index="gene_name").empty