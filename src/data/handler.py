from dataclasses import dataclass

@dataclass
class Handler:
  def __post_init__(self):
            for (name, field_type) in self.__annotations__.items():
                if not isinstance(self.__dict__[name], field_type):
                    current_type = type(self.__dict__[name])
                    raise TypeError(
                        f"The field `{name}` was assigned by `{current_type}` instead of `{field_type}`"
                    )

  def handler():
    return {
      'tst': True
    }