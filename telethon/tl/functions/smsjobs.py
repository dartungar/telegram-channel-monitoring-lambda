"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from ...tl.tlobject import TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime


class FinishJobRequest(TLRequest):
    CONSTRUCTOR_ID = 0x4f1ebf24
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, job_id: str, error: Optional[str]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.job_id = job_id
        self.error = error

    def to_dict(self):
        return {
            '_': 'FinishJobRequest',
            'job_id': self.job_id,
            'error': self.error
        }

    def _bytes(self):
        return b''.join((
            b'$\xbf\x1eO',
            struct.pack('<I', (0 if self.error is None or self.error is False else 1)),
            self.serialize_bytes(self.job_id),
            b'' if self.error is None or self.error is False else (self.serialize_bytes(self.error)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _job_id = reader.tgread_string()
        if flags & 1:
            _error = reader.tgread_string()
        else:
            _error = None
        return cls(job_id=_job_id, error=_error)


class GetSmsJobRequest(TLRequest):
    CONSTRUCTOR_ID = 0x778d902f
    SUBCLASS_OF_ID = 0x1f24187e

    def __init__(self, job_id: str):
        """
        :returns SmsJob: Instance of SmsJob.
        """
        self.job_id = job_id

    def to_dict(self):
        return {
            '_': 'GetSmsJobRequest',
            'job_id': self.job_id
        }

    def _bytes(self):
        return b''.join((
            b'/\x90\x8dw',
            self.serialize_bytes(self.job_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _job_id = reader.tgread_string()
        return cls(job_id=_job_id)


class GetStatusRequest(TLRequest):
    CONSTRUCTOR_ID = 0x10a698e8
    SUBCLASS_OF_ID = 0xcd8f2b25

    def to_dict(self):
        return {
            '_': 'GetStatusRequest'
        }

    def _bytes(self):
        return b''.join((
            b'\xe8\x98\xa6\x10',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class IsEligibleToJoinRequest(TLRequest):
    CONSTRUCTOR_ID = 0xedc39d0
    SUBCLASS_OF_ID = 0x5eb760a6

    def to_dict(self):
        return {
            '_': 'IsEligibleToJoinRequest'
        }

    def _bytes(self):
        return b''.join((
            b'\xd09\xdc\x0e',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class JoinRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa74ece2d
    SUBCLASS_OF_ID = 0xf5b399ac

    def to_dict(self):
        return {
            '_': 'JoinRequest'
        }

    def _bytes(self):
        return b''.join((
            b'-\xceN\xa7',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class LeaveRequest(TLRequest):
    CONSTRUCTOR_ID = 0x9898ad73
    SUBCLASS_OF_ID = 0xf5b399ac

    def to_dict(self):
        return {
            '_': 'LeaveRequest'
        }

    def _bytes(self):
        return b''.join((
            b's\xad\x98\x98',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class UpdateSettingsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x93fa0bf
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, allow_international: Optional[bool]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.allow_international = allow_international

    def to_dict(self):
        return {
            '_': 'UpdateSettingsRequest',
            'allow_international': self.allow_international
        }

    def _bytes(self):
        return b''.join((
            b'\xbf\xa0?\t',
            struct.pack('<I', (0 if self.allow_international is None or self.allow_international is False else 1)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _allow_international = bool(flags & 1)
        return cls(allow_international=_allow_international)
