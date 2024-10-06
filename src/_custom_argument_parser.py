from __future__ import annotations

import argparse


class CustomArgumentParser(argparse.ArgumentParser):
    def add_argument(
        self,
        *args,
        **kwargs,
    ):
        """
        Adds an argument to the parser, converting boolean types to a custom
        string-to-boolean function.
        :return: None
        """
        if kwargs.get("type") is bool:
            kwargs["type"] = self._str2bool
        super().add_argument(
            *args,
            **kwargs,
        )

    def _str2bool(self, v):
        """
        Converts a string representation of a boolean value to a boolean type.
        :param v: The input value to be converted to a boolean.
        :return: True or False based on the input string.
        """
        if isinstance(v, bool):
            return v
        if v.lower() in ("yes", "true", "t", "y", "1"):
            return True
        elif v.lower() in ("no", "false", "f", "n", "0"):
            return False
        else:
            raise argparse.ArgumentTypeError(
                f"Boolean value expected got {v}."
            )
