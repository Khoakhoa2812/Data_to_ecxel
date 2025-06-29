from loguru import logger as _logger
import sys
import uuid
from contextvars import ContextVar

# Per-request trace ID
trace_id_ctx_var: ContextVar[str] = ContextVar("trace_id", default=None)


def get_trace_id() -> str:
    return trace_id_ctx_var.get() or "no-trace-id"


# NestJS-inspired log format
LOG_FORMAT = (
    "<green>[FastAPI]</green> {time:YYYY-MM-DD HH:mm:ss} | "
    "<level>{level: <5}</level> "
    "[{extra[trace_id]}] "
    "<cyan>{message}</cyan>"
)

_logger.remove()
_logger.add(sys.stdout, level="DEBUG", format=LOG_FORMAT, backtrace=False, diagnose=False)


class ContextualLogger:
    def __getattr__(self, name):
        return getattr(_logger.bind(trace_id=get_trace_id()), name)


logger = ContextualLogger()
