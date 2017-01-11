# Micro-img

[![Join the chat at https://gitter.im/microimg/Lobby](https://badges.gitter.im/microimg/Lobby.svg)](https://gitter.im/microimg/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Tiny image previews for everyone


## V0 : proposed scenario

Here are some diagarams proposing a simplified scenario:

### Uploading an image

![sequence_upload](https://raw.githubusercontent.com/RaedsLab/microimg/master/doc/img/seq_upload.png)

When the user uploads an image, the backend saves the full-resolution copy the way it usually does.

However it also queries, the microIMG server for the microIMG. The response should be a JSON string, that contains a "header" and a "body".

For the same configuration, the "header" value should always be the same. This can be used to error-check the set-up.

<hr>

### Displaying an image

![sequence_display](https://raw.githubusercontent.com/RaedsLab/microimg/master/doc/img/seq_get.png)

When the user required the content, the content gets sent with the microIMG-header pre-attached.

The microIMG is the requested, and when it gets to the browser, it gets reconstructed as a base64 image.

Once the content is ready, it can request the full resolution image, to replace the microIMG. 
