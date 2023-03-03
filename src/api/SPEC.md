# API Specification

This document describes the API specification for the Speaking-Portal project.

## Endpoints

1. ```/text-speech```

    This endpoint converts the text to speech and returns the audio file using Kukarella's service.
    Audio file is saved in google cloud storage and the link is returned.

    **Parameters**

    | Name | Type | Description |
    | ---- | ---- | ----------- |
    | text | string | The text to be converted to audio. |

    **Response**

    | Name | Type | Description |
    | ---- | ---- | ----------- |
    | audio | binary | The audio file for the given text. |

2. ```/gentle-out```

    This endpoint returns the gentle output for the given audio file and text file.
    The audio file can be accessed from the google cloud storage using the link returned by the ```/get-speech``` endpoint.


    **Parameters**

    | Name | Type | Description |
    | ---- | ---- | ----------- |
    | audio | binary | The audio file for which gentle output is required. |
    | text | string | The text file for which gentle output is required. |

    **Response**

    | Name | Type | Description |
    | ---- | ---- | ----------- |
    | gentle_out | json | The gentle output for the given audio file. |

3. ```/get-avatar```

    This endpoint returns info about the avatar that was selected such mouth coordinates, eye coordinates, storage URL in google cloud storage, etc, and on the backend it prepare the frames that might be use to generate the video in a folder on google cloud storage.

    **Parameters**

    | Name | Type | Description |
    | ---- | ---- | ----------- |

    **Response**

    | Name | Type | Description |
    | ---- | ---- | ----------- |
    | avatar | json | The avatar info. |

4. ```/generate-video```

    This endpoint returns the video file for the given audio file, gentle output and avatar frames using the lazykh library.

    **Parameters**

    | Name | Type | Description |
    | ---- | ---- | ----------- |
    | audio | binary | The audio file for which video is required. |
    | gentle_out | json | The gentle output for the given audio file. |

    **Response**

    | Name | Type | Description |
    | ---- | ---- | ----------- |
    | video | binary | The video file for the given audio file. |