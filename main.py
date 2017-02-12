#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print ('参数错误')
    sys.exit()

import xml.dom.minidom


drawable = xml.dom.minidom.parse(sys.argv[1])
drawable_vector = drawable.documentElement
drawable_paths = drawable_vector.getElementsByTagName('path')

svg = xml.dom.minidom.Document()
svg_svg = svg.createElement('svg') 
svg_svg.setAttribute('version', '1.1')
svg_svg.setAttribute('xmlns', "http://www.w3.org/2000/svg")
svg_svg.setAttribute('xmlns:xlink', "http://www.w3.org/1999/xlink")
svg_svg.setAttribute('x', "0px")
svg_svg.setAttribute('y', "0px")
svg_svg.setAttribute('viewBox', "0 0 " + drawable_vector.getAttribute('android:viewportWidth') + " " + drawable_vector.getAttribute('android:viewportHeight'))
svg_svg.setAttribute('enable-background', "new 0 0 " + drawable_vector.getAttribute('android:viewportWidth') + " " + drawable_vector.getAttribute('android:viewportHeight'))
svg_svg.setAttribute('xml:space', "preserve")
svg.appendChild(svg_svg)

for drawable_path in drawable_paths :
    svg_path = svg.createElement('path')
    svg_path.setAttribute('d', drawable_path.getAttribute('android:pathData'))
    svg_path.setAttribute('fill', drawable_path.getAttribute('android:fillColor'))
    svg_path.setAttribute('stroke', drawable_path.getAttribute('android:strokeColor'))
    svg_path.setAttribute('stroke-width', drawable_path.getAttribute('android:strokeWidth'))
    svg_path.setAttribute('stroke-miterlimit', drawable_path.getAttribute('android:strokeMiterLimit'))
    svg_svg.appendChild(svg_path)


svg.writexml(sys.stdout, indent='\t', addindent='\t', newl='\n', encoding="utf-8")

