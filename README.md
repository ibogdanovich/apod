# NASA:Astronomy Picture of the Day script
This short script allow you to get the link of "Astronomy Photo of the Day" (APOD) through api.nasa.gov

## How it works
Script without any args return APOD URL. For additional data use corresponding args.

##Arguments
Script always return URL in case of arguments return additional information.
```
--hires, -r: show the likt to the photo in high resolution
--info','-i': show full information about photo
--title','-t: show photo title
--expl','-e: show explanation text
```

##Configuration
Get your own API key on [NASA OpenAPIs](https://api.nasa.gov) and put it into api_key in config.py.
