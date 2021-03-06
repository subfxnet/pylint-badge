import argparse

from pylint.lint import Run

def get_color(score):
    colors = {
        "brightgreen":    "#4c1",
        "green":          "#97CA00",
        "yellow":         "#dfb317",
        "yellowgreen":    "#a4a61d",
        "orange":         "#fe7d37",
        "red":            "#e05d44",
        "bloodred":       "#ff0000", 
        "blue":           "#007ec6",
        "grey":           "#555",
        "gray":           "#555",
        "lightgrey":      "#9f9f9f",
        "lightgray":      "#9f9f9f" 
    }

    if score > 9.0:
	    return colors['brightgreen']
    if score > 8.0:
        return colors['green']  
    if score > 7.5:
        return colors['yellowgreen']  
    if score > 6.6:
        return colors['yellow']   
    if score > 5.0:
        return colors['orange']     
    if score > 3.0:
	    return colors['red']
    return colors['bloodred']


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("file_to_lint")
    args = parser.parse_args()
    file_to_lint = args.file_to_lint
    
    score = round(Run([file_to_lint], do_exit=False).linter.stats['global_note'], 2)

    template = """
<svg xmlns="http://www.w3.org/2000/svg" width="85" height="20">
  <linearGradient id="a" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <rect rx="3" width="85" height="20" fill="#555"/>
  <rect rx="3" x="50" width="35" height="20" fill="{color}"/>
  <path fill="{color}" d="M50 0h4v20h-4z"/>
  <rect rx="3" width="85" height="20" fill="url(#a)"/>
  <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
    <text x="25" y="15" fill="#010101" fill-opacity=".3">pylint</text>
    <text x="25" y="14">pylint</text>
    <text x="67" y="15" fill="#010101" fill-opacity=".3">{score}</text>
    <text x="67" y="14">{score}</text>
  </g>
</svg>
"""
    color = get_color(float(score))

    with open("pylint.svg", 'w') as score_file:
        score_file.write(template.format(score=score, color=color))

if __name__ == "__main__":
    main()
