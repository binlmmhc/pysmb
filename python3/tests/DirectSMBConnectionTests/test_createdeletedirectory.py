# -*- coding: utf-8 -*-

import os, time, random
from smb.SMBConnection import SMBConnection
from smb.smb2_constants import SMB2_DIALECT_2
from .util import getConnectionInfo
from nose.tools import with_setup
from smb import smb_structs

conn = None

def setup_func_SMB1():
    global conn
    smb_structs.SUPPORT_SMB2 = smb_structs.SUPPORT_SMB2x = False

    info = getConnectionInfo()
    conn = SMBConnection(info['user'], info['password'], info['client_name'], info['server_name'], use_ntlm_v2 = True, is_direct_tcp = True)
    assert conn.connect(info['server_ip'], info['server_port'])

def setup_func_SMB2():
    global conn
    smb_structs.SUPPORT_SMB2 = True
    smb_structs.SUPPORT_SMB2x = False

    info = getConnectionInfo()
    conn = SMBConnection(info['user'], info['password'], info['client_name'], info['server_name'], use_ntlm_v2 = True, is_direct_tcp = True)
    assert conn.connect(info['server_ip'], info['server_port'])

def setup_func_SMB2x():
    global conn
    smb_structs.SUPPORT_SMB2 = smb_structs.SUPPORT_SMB2x = True

    info = getConnectionInfo()
    conn = SMBConnection(info['user'], info['password'], info['client_name'], info['server_name'], use_ntlm_v2 = True, is_direct_tcp = True)
    assert conn.connect(info['server_ip'], info['server_port'])

def teardown_func():
    global conn
    conn.close()

@with_setup(setup_func_SMB1, teardown_func)
def test_english_directory_SMB1():
    global conn

    path = os.sep + 'TestDir %d-%d' % ( time.time(), random.randint(0, 1000) )
    conn.createDirectory('smbtest', path)

    entries = conn.listPath('smbtest', os.path.dirname(path.replace('/', os.sep)))
    names = map(lambda e: e.filename, entries)
    assert os.path.basename(path.replace('/', os.sep)) in names

    conn.deleteDirectory('smbtest', path)

    entries = conn.listPath('smbtest', os.path.dirname(path.replace('/', os.sep)))
    names = map(lambda e: e.filename, entries)
    assert os.path.basename(path.replace('/', os.sep)) not in names

@with_setup(setup_func_SMB2, teardown_func)
def test_english_directory_SMB2():
    global conn
    assert conn.smb2_dialect == SMB2_DIALECT_2

    path = os.sep + 'TestDir %d-%d' % ( time.time(), random.randint(0, 1000) )
    conn.createDirectory('smbtest', path)

    entries = conn.listPath('smbtest', os.path.dirname(path.replace('/', os.sep)))
    names = map(lambda e: e.filename, entries)
    assert os.path.basename(path.replace('/', os.sep)) in names

    conn.deleteDirectory('smbtest', path)

    entries = conn.listPath('smbtest', os.path.dirname(path.replace('/', os.sep)))
    names = map(lambda e: e.filename, entries)
    assert os.path.basename(path.replace('/', os.sep)) not in names

@with_setup(setup_func_SMB2x, teardown_func)
def test_english_directory_SMB2x():
    global conn
    assert conn.smb2_dialect != SMB2_DIALECT_2

    path = os.sep + 'TestDir %d-%d' % ( time.time(), random.randint(0, 1000) )
    conn.createDirectory('smbtest', path)

    entries = conn.listPath('smbtest', os.path.dirname(path.replace('/', os.sep)))
    names = map(lambda e: e.filename, entries)
    assert os.path.basename(path.replace('/', os.sep)) in names

    conn.deleteDirectory('smbtest', path)

    entries = conn.listPath('smbtest', os.path.dirname(path.replace('/', os.sep)))
    names = map(lambda e: e.filename, entries)
    assert os.path.basename(path.replace('/', os.sep)) not in names

@with_setup(setup_func_SMB1, teardown_func)
def test_unicode_directory_SMB1():
    global conn

    path = os.sep + u'文件夹创建 %d-%d' % ( time.time(), random.randint(0, 1000) )
    conn.createDirectory('smbtest', path)

    entries = conn.listPath('smbtest', os.path.dirname(path.replace('/', os.sep)))
    names = map(lambda e: e.filename, entries)
    assert os.path.basename(path.replace('/', os.sep)) in names

    conn.deleteDirectory('smbtest', path)

    entries = conn.listPath('smbtest', os.path.dirname(path.replace('/', os.sep)))
    names = map(lambda e: e.filename, entries)
    assert os.path.basename(path.replace('/', os.sep)) not in names

@with_setup(setup_func_SMB2, teardown_func)
def test_unicode_directory_SMB2():
    global conn
    assert conn.smb2_dialect == SMB2_DIALECT_2

    path = os.sep + u'文件夹创建 %d-%d' % ( time.time(), random.randint(0, 1000) )
    conn.createDirectory('smbtest', path)

    entries = conn.listPath('smbtest', os.path.dirname(path.replace('/', os.sep)))
    names = map(lambda e: e.filename, entries)
    assert os.path.basename(path.replace('/', os.sep)) in names

    conn.deleteDirectory('smbtest', path)

    entries = conn.listPath('smbtest', os.path.dirname(path.replace('/', os.sep)))
    names = map(lambda e: e.filename, entries)
    assert os.path.basename(path.replace('/', os.sep)) not in names

@with_setup(setup_func_SMB2x, teardown_func)
def test_unicode_directory_SMB2x():
    global conn
    assert conn.smb2_dialect != SMB2_DIALECT_2

    path = os.sep + u'文件夹创建 %d-%d' % ( time.time(), random.randint(0, 1000) )
    conn.createDirectory('smbtest', path)

    entries = conn.listPath('smbtest', os.path.dirname(path.replace('/', os.sep)))
    names = map(lambda e: e.filename, entries)
    assert os.path.basename(path.replace('/', os.sep)) in names

    conn.deleteDirectory('smbtest', path)

    entries = conn.listPath('smbtest', os.path.dirname(path.replace('/', os.sep)))
    names = map(lambda e: e.filename, entries)
    assert os.path.basename(path.replace('/', os.sep)) not in names
