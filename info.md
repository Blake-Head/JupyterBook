To update this text book, run the following command:
    jupyter-book build UniversityPhysics

To publish to github pages, run the following:
    ghp-import -n -p -f UniversityPhysics/_build/html

The book is linked here
    https://blake-head.github.io/University-Physics/

To convert manim video to gif, run something like the following
ffmpeg -i media/videos/integration/2160p60/AreaUnderCurve.mp4 -vf "fps=60,scale=3840:-1:flags=lanczos" -loop 0 -c:v gif -q:v 5 output.gif