"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from ...tl.tlobject import TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime
if TYPE_CHECKING:
    from ...tl.types import TypeInputChannel, TypeInputCheckPasswordSRP, TypeInputPeer



class GetBroadcastRevenueStatsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x75dfb671
    SUBCLASS_OF_ID = 0x2cee3078

    def __init__(self, channel: 'TypeInputChannel', dark: Optional[bool]=None):
        """
        :returns stats.BroadcastRevenueStats: Instance of BroadcastRevenueStats.
        """
        self.channel = channel
        self.dark = dark

    async def resolve(self, client, utils):
        self.channel = utils.get_input_channel(await client.get_input_entity(self.channel))

    def to_dict(self):
        return {
            '_': 'GetBroadcastRevenueStatsRequest',
            'channel': self.channel.to_dict() if isinstance(self.channel, TLObject) else self.channel,
            'dark': self.dark
        }

    def _bytes(self):
        return b''.join((
            b'q\xb6\xdfu',
            struct.pack('<I', (0 if self.dark is None or self.dark is False else 1)),
            self.channel._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _dark = bool(flags & 1)
        _channel = reader.tgread_object()
        return cls(channel=_channel, dark=_dark)


class GetBroadcastRevenueTransactionsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x69280f
    SUBCLASS_OF_ID = 0x676ea15

    def __init__(self, channel: 'TypeInputChannel', offset: int, limit: int):
        """
        :returns stats.BroadcastRevenueTransactions: Instance of BroadcastRevenueTransactions.
        """
        self.channel = channel
        self.offset = offset
        self.limit = limit

    async def resolve(self, client, utils):
        self.channel = utils.get_input_channel(await client.get_input_entity(self.channel))

    def to_dict(self):
        return {
            '_': 'GetBroadcastRevenueTransactionsRequest',
            'channel': self.channel.to_dict() if isinstance(self.channel, TLObject) else self.channel,
            'offset': self.offset,
            'limit': self.limit
        }

    def _bytes(self):
        return b''.join((
            b'\x0f(i\x00',
            self.channel._bytes(),
            struct.pack('<i', self.offset),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        _channel = reader.tgread_object()
        _offset = reader.read_int()
        _limit = reader.read_int()
        return cls(channel=_channel, offset=_offset, limit=_limit)


class GetBroadcastRevenueWithdrawalUrlRequest(TLRequest):
    CONSTRUCTOR_ID = 0x2a65ef73
    SUBCLASS_OF_ID = 0xd15cc8e5

    def __init__(self, channel: 'TypeInputChannel', password: 'TypeInputCheckPasswordSRP'):
        """
        :returns stats.BroadcastRevenueWithdrawalUrl: Instance of BroadcastRevenueWithdrawalUrl.
        """
        self.channel = channel
        self.password = password

    async def resolve(self, client, utils):
        self.channel = utils.get_input_channel(await client.get_input_entity(self.channel))

    def to_dict(self):
        return {
            '_': 'GetBroadcastRevenueWithdrawalUrlRequest',
            'channel': self.channel.to_dict() if isinstance(self.channel, TLObject) else self.channel,
            'password': self.password.to_dict() if isinstance(self.password, TLObject) else self.password
        }

    def _bytes(self):
        return b''.join((
            b's\xefe*',
            self.channel._bytes(),
            self.password._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _channel = reader.tgread_object()
        _password = reader.tgread_object()
        return cls(channel=_channel, password=_password)


class GetBroadcastStatsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xab42441a
    SUBCLASS_OF_ID = 0x7ff25428

    def __init__(self, channel: 'TypeInputChannel', dark: Optional[bool]=None):
        """
        :returns stats.BroadcastStats: Instance of BroadcastStats.
        """
        self.channel = channel
        self.dark = dark

    async def resolve(self, client, utils):
        self.channel = utils.get_input_channel(await client.get_input_entity(self.channel))

    def to_dict(self):
        return {
            '_': 'GetBroadcastStatsRequest',
            'channel': self.channel.to_dict() if isinstance(self.channel, TLObject) else self.channel,
            'dark': self.dark
        }

    def _bytes(self):
        return b''.join((
            b'\x1aDB\xab',
            struct.pack('<I', (0 if self.dark is None or self.dark is False else 1)),
            self.channel._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _dark = bool(flags & 1)
        _channel = reader.tgread_object()
        return cls(channel=_channel, dark=_dark)


class GetMegagroupStatsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xdcdf8607
    SUBCLASS_OF_ID = 0x5b59be8d

    def __init__(self, channel: 'TypeInputChannel', dark: Optional[bool]=None):
        """
        :returns stats.MegagroupStats: Instance of MegagroupStats.
        """
        self.channel = channel
        self.dark = dark

    async def resolve(self, client, utils):
        self.channel = utils.get_input_channel(await client.get_input_entity(self.channel))

    def to_dict(self):
        return {
            '_': 'GetMegagroupStatsRequest',
            'channel': self.channel.to_dict() if isinstance(self.channel, TLObject) else self.channel,
            'dark': self.dark
        }

    def _bytes(self):
        return b''.join((
            b'\x07\x86\xdf\xdc',
            struct.pack('<I', (0 if self.dark is None or self.dark is False else 1)),
            self.channel._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _dark = bool(flags & 1)
        _channel = reader.tgread_object()
        return cls(channel=_channel, dark=_dark)


class GetMessagePublicForwardsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x5f150144
    SUBCLASS_OF_ID = 0xa7283211

    def __init__(self, channel: 'TypeInputChannel', msg_id: int, offset: str, limit: int):
        """
        :returns stats.PublicForwards: Instance of PublicForwards.
        """
        self.channel = channel
        self.msg_id = msg_id
        self.offset = offset
        self.limit = limit

    async def resolve(self, client, utils):
        self.channel = utils.get_input_channel(await client.get_input_entity(self.channel))

    def to_dict(self):
        return {
            '_': 'GetMessagePublicForwardsRequest',
            'channel': self.channel.to_dict() if isinstance(self.channel, TLObject) else self.channel,
            'msg_id': self.msg_id,
            'offset': self.offset,
            'limit': self.limit
        }

    def _bytes(self):
        return b''.join((
            b'D\x01\x15_',
            self.channel._bytes(),
            struct.pack('<i', self.msg_id),
            self.serialize_bytes(self.offset),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        _channel = reader.tgread_object()
        _msg_id = reader.read_int()
        _offset = reader.tgread_string()
        _limit = reader.read_int()
        return cls(channel=_channel, msg_id=_msg_id, offset=_offset, limit=_limit)


class GetMessageStatsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb6e0a3f5
    SUBCLASS_OF_ID = 0x9604a322

    def __init__(self, channel: 'TypeInputChannel', msg_id: int, dark: Optional[bool]=None):
        """
        :returns stats.MessageStats: Instance of MessageStats.
        """
        self.channel = channel
        self.msg_id = msg_id
        self.dark = dark

    async def resolve(self, client, utils):
        self.channel = utils.get_input_channel(await client.get_input_entity(self.channel))

    def to_dict(self):
        return {
            '_': 'GetMessageStatsRequest',
            'channel': self.channel.to_dict() if isinstance(self.channel, TLObject) else self.channel,
            'msg_id': self.msg_id,
            'dark': self.dark
        }

    def _bytes(self):
        return b''.join((
            b'\xf5\xa3\xe0\xb6',
            struct.pack('<I', (0 if self.dark is None or self.dark is False else 1)),
            self.channel._bytes(),
            struct.pack('<i', self.msg_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _dark = bool(flags & 1)
        _channel = reader.tgread_object()
        _msg_id = reader.read_int()
        return cls(channel=_channel, msg_id=_msg_id, dark=_dark)


class GetStoryPublicForwardsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa6437ef6
    SUBCLASS_OF_ID = 0xa7283211

    def __init__(self, peer: 'TypeInputPeer', id: int, offset: str, limit: int):
        """
        :returns stats.PublicForwards: Instance of PublicForwards.
        """
        self.peer = peer
        self.id = id
        self.offset = offset
        self.limit = limit

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetStoryPublicForwardsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': self.id,
            'offset': self.offset,
            'limit': self.limit
        }

    def _bytes(self):
        return b''.join((
            b'\xf6~C\xa6',
            self.peer._bytes(),
            struct.pack('<i', self.id),
            self.serialize_bytes(self.offset),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _id = reader.read_int()
        _offset = reader.tgread_string()
        _limit = reader.read_int()
        return cls(peer=_peer, id=_id, offset=_offset, limit=_limit)


class GetStoryStatsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x374fef40
    SUBCLASS_OF_ID = 0x8b4d43d4

    def __init__(self, peer: 'TypeInputPeer', id: int, dark: Optional[bool]=None):
        """
        :returns stats.StoryStats: Instance of StoryStats.
        """
        self.peer = peer
        self.id = id
        self.dark = dark

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetStoryStatsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': self.id,
            'dark': self.dark
        }

    def _bytes(self):
        return b''.join((
            b'@\xefO7',
            struct.pack('<I', (0 if self.dark is None or self.dark is False else 1)),
            self.peer._bytes(),
            struct.pack('<i', self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _dark = bool(flags & 1)
        _peer = reader.tgread_object()
        _id = reader.read_int()
        return cls(peer=_peer, id=_id, dark=_dark)


class LoadAsyncGraphRequest(TLRequest):
    CONSTRUCTOR_ID = 0x621d5fa0
    SUBCLASS_OF_ID = 0x9b903153

    def __init__(self, token: str, x: Optional[int]=None):
        """
        :returns StatsGraph: Instance of either StatsGraphAsync, StatsGraphError, StatsGraph.
        """
        self.token = token
        self.x = x

    def to_dict(self):
        return {
            '_': 'LoadAsyncGraphRequest',
            'token': self.token,
            'x': self.x
        }

    def _bytes(self):
        return b''.join((
            b'\xa0_\x1db',
            struct.pack('<I', (0 if self.x is None or self.x is False else 1)),
            self.serialize_bytes(self.token),
            b'' if self.x is None or self.x is False else (struct.pack('<q', self.x)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _token = reader.tgread_string()
        if flags & 1:
            _x = reader.read_long()
        else:
            _x = None
        return cls(token=_token, x=_x)

